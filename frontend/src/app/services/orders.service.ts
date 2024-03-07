import { Injectable, signal } from '@angular/core';
import { Order } from '../shared/models/order.model';

@Injectable({
  providedIn: 'root'
})
export class OrdersService {

  orders = signal<Order>;
  tableSelected = signal<number>(0);

  constructor() { }

  updateOrder(table: number) {
    this.tableSelected.update(last => table)
  }

  saveOrder(order: Order) {

  }

}
