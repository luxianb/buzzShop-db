from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import CartItem, Product, Store
from .serializers import CartDisplaySerializer, CartSerializer, ProductSerializer, StoreSerializer


# Create your views here.
class StoreView( ):
  def get(self, req):
    return Response({"hello":"world", "method": req.method})

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [permissions.AllowAny]

# ------------- Store Views ------------- #
@api_view(["GET"]) 
@permission_classes([permissions.AllowAny])
def store_list(request):
  stores = Store.objects.all()
  serializer = StoreSerializer(stores, many=True)
  return Response(serializer.data)


@api_view(['GET']) 
@permission_classes([permissions.AllowAny])
def store_view(request, pk):
  store = Store.objects.get(id=pk)

  serializer = StoreSerializer(store, many=False)
  return Response(serializer.data)



@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def store_add(request):
  serializer = StoreSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "DELETE"])
@permission_classes([permissions.IsAuthenticated])
def store_updateDelete(request, pk):
  store = Store.objects.get(id=pk)

  if request.method == "PUT":
    serializer = StoreSerializer(instance=store, data=request.data)
    if serializer.is_valid():
      serializer.save()

    return Response(serializer.data)
  
  elif request.method == "DELETE":
    store.delete()

    return Response(store.data)


# ------------- Product Views ------------- #
@api_view(["GET"]) 
@permission_classes([permissions.AllowAny])
def products_list(request):
  products = Product.objects.all()
  serializer = ProductSerializer(products, many=True)
  return Response(serializer.data)


@api_view(['GET']) 
@permission_classes([permissions.AllowAny])
def product_view(request, pk):
  product = Product.objects.get(id=pk)

  serializer = ProductSerializer(product, many=False)
  return Response(serializer.data)



@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def product_add(request):
  serializer = ProductSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "DELETE", "GET"])
@permission_classes([permissions.AllowAny])
def product_updateDelete(request, pk):
  product = Product.objects.get(id=pk)

  if request.method == "GET":
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

  if request.method == "PUT":
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
      serializer.save()

    return Response(serializer.data)
  
  elif request.method == "DELETE":
    product.delete()

    return Response(product.data)

# ------------- Cart Views ------------- #
@api_view(["GET"]) 
@permission_classes([permissions.IsAuthenticated])
def user_cart(request, user_id):
  cart_items = CartItem.objects.filter(user=user_id)
  print(cart_items)
  serializer = CartDisplaySerializer(cart_items, many=True)
  return Response(serializer.data)


@api_view(['GET']) 
@permission_classes([permissions.IsAuthenticated])
def cart_item(request, item_id):
  cart_item = CartItem.objects.get(id=item_id)

  serializer = CartDisplaySerializer(cart_item, many=False)
  return Response(serializer.data)



@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def cart_add(request):
  body = request.data
  item_exists = CartItem.objects.filter(user=body['user'], product=body['product'])

  # If user already has item, add increment to amount
  if item_exists:
    existing_item = CartItem.objects.get(user=body['user'], product=body['product'])
    body['amount'] += existing_item.amount
    serializer = CartSerializer(instance=existing_item, data=body)

    if serializer.is_valid():
      serializer.save()
    
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

  # # Else create new cart item
  else:
    serializer = CartSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

  # return Response("Function called")
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(["PUT", "DELETE"])
@permission_classes([permissions.IsAuthenticated])
def cart_updateDelete(request, item_id):
  cart_item = CartItem.objects.get(id=item_id)

  if request.method == "PUT":
    serializer = CartSerializer(instance=cart_item, data=request.data)
    if serializer.is_valid():
      serializer.save()

      return Response(serializer.data, status=status.HTTP_200_OK)
  
  elif request.method == "DELETE":
    cart_item.delete()

    return Response("Item removed", status=status.HTTP_200_OK)
