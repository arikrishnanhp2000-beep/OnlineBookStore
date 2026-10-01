from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Book, Cart, Order, OrderItem

def home(request):
    query = request.GET.get('q')

    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    return render(
        request,
        'store/home.html',
        {
            'books': books,
            'query': query
        }
    )
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)


    return render(
        request,
        'store/book_detail.html',
        {
            'book': book
        }
    )
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']


        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect('home')

    return render(
        request,
        'store/register.html'
    )
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(
            request,
            'store/login.html',
            {
                'error': 'Invalid username or password'
            }
        )

    return render(
        request,
        'store/login.html'
    )

def user_logout(request):
    logout(request)
    return redirect('home')

def add_to_cart(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    
    book = get_object_or_404(
        Book,
        id=id
    )

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        book=book
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    cart_items = Cart.objects.filter(
        user=request.user
    )

    total = sum(
        item.book.price * item.quantity
        for item in cart_items
    )
    return render(
        request,
        'store/cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )
    
def remove_from_cart(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    cart_item = get_object_or_404(
        Cart,
        id=id,
        user=request.user
    )

    cart_item.delete()

    return redirect('cart')


def update_cart(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    cart_item = get_object_or_404(
        Cart,
        id=id,
        user=request.user
    )

    if request.method == 'POST':
        quantity = int(request.POST['quantity'])

        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('cart')

def place_order(request):
    if not request.user.is_authenticated:
        return redirect('login')
    cart_items = Cart.objects.filter(
        user=request.user
    )

    if not cart_items.exists():
        return redirect('cart')

    total = sum(
        item.book.price * item.quantity
        for item in cart_items
    )

    order = Order.objects.create(
        user=request.user,
        total_amount=total
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            book=item.book,
            quantity=item.quantity,
            price=item.book.price
        )

        item.book.stock -= item.quantity
        item.book.save()

    cart_items.delete()

    return redirect(
        'order_success',
        order_id=order.id
    )
def order_success(request, order_id):
    if not request.user.is_authenticated:
        return redirect('login')
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(
        request,
        'store/order_success.html',
        {
            'order': order
        }
    )
def my_orders(request):
    if not request.user.is_authenticated:
        return redirect('login')
    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')
    return render(
        request,
        'store/my_orders.html',
        {
            'orders': orders
        }
    )

