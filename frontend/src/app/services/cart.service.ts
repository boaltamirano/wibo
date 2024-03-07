import { Injectable, computed, inject, signal } from '@angular/core';
import { Menu } from '../shared/models/menu.model';
import { UsersService } from './users.service';
import { OrdersService } from './orders.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { firstValueFrom } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CartService {

  private userService = inject(UsersService)
  private orderService = inject(OrdersService)
  rutaApi = "http://localhost:8000";

  cart = signal<Menu[]>([]);
  subTotal = computed(() => {
    const cart = this.cart();
    return parseFloat((cart.reduce((total, menu) => total + menu.total, 0)).toFixed(2))
  })

  serviceCharge = computed(() => {
    const cart = this.cart();
    const subtotal = cart.reduce((total, menu) => total + menu.total, 0)
    return parseFloat(((subtotal * 5) / 100).toFixed(2));
  })

  total = computed(() => {
    const cart = this.cart();
    const subtotal = cart.reduce((total, menu) => total + menu.total, 0)
    const serviceCharge = (subtotal * 5) / 100;
    return parseFloat((subtotal + serviceCharge).toFixed(2));
  })

  constructor(private http: HttpClient) {}

  addToCart(menu: Menu) {
    const existingMenuIndex = this.cart().findIndex(m => m.id === menu.id);

    if (existingMenuIndex !== -1) {
      this.cart.update(state => {
        const updatedCart = [...state];
        updatedCart[existingMenuIndex] = {
          ...updatedCart[existingMenuIndex],
          amount: (updatedCart[existingMenuIndex].amount || 0) + 1,
          total: parseFloat(((updatedCart[existingMenuIndex].total || 0) + menu.price).toFixed(2))
        };
        return updatedCart;
      });
    } else {
      const newMenu = { ...menu, amount: 1, total: menu.price };
      this.cart.update(state => [...state, newMenu]);
    }
  }

  async saveOrder() {
    const carts = this.cart();
    const newCart = carts.map(cart => {
      return {
        menu: cart.id,
        amount: cart.amount,
        subtotal: cart.total
      };
    })

    const userLS = localStorage.getItem('user');
    let user;
    if (userLS !== null) {
      user = JSON.parse(userLS);
    } else {
      console.log("La clave 'miObjeto' no existe en el localStorage o su valor es null.");
    }


    const order = {
      table: this.orderService.tableSelected(),
      menus: newCart,
      subtotal: this.subTotal(),
      total: this.total(),
      tip: this.serviceCharge(),
      state: 'completed',
      user: user?.id
    }

    const httpOptions = {
      headers: new HttpHeaders({
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXJAdGVzdC5jb20iLCJleHAiOjE3MDk4MTQzOTl9.vq2RYwf6RJl4iITCO3RLOKLRrsXGV2rpx7HQjzK1vj0'
      })
    };
    const orders = firstValueFrom(
      this.http.post(`${this.rutaApi}/orders`, order, httpOptions)
    )

  }
}
