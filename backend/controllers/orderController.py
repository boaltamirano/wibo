from services.orderService import OrderService

class OrderController:

    def create_order(order):
        return OrderService.create_order(order)
    
    def get_orders(page, limit):
        return OrderService.get_orders(page, limit)
    
    def get_order_by_id(id):
        return OrderService.get_order_by_id(id)
    
    def get_order_by_user(user_id, page, limit):
        return OrderService.get_order_by_user(user_id, page, limit)
    
    def delete_order(id):
        return OrderService.delete_order(id)