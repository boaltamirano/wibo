import { Component, inject } from '@angular/core';
import { OrdersService } from '../../../../services/orders.service';
import { MenuSelectedComponent } from '../../components/menu-selected/menu-selected.component';
import { CartService } from '../../../../services/cart.service';
import { CommonModule } from '@angular/common';
import { Order } from '../../../../shared/models/order.model';
import { Router } from '@angular/router';

@Component({
  selector: 'app-page-selected',
  standalone: true,
  imports: [MenuSelectedComponent, CommonModule],
  templateUrl: './page-selected.component.html',
  styleUrl: './page-selected.component.css'
})
export class PageSelectedComponent {
  private tableService = inject(OrdersService)
  private cartService = inject(CartService)

  table = this.tableService.tableSelected;
  cart = this.cartService.cart;
  serviceCharge = this.cartService.serviceCharge;
  subtotal = this.cartService.subTotal;
  total = this.cartService.total;
  validation = false;
  selected = false;
  message = "Seleccione la mesa para poder continuar"

  constructor(
    private router: Router
  ) { }

  async saveOrder() {
    this.selected = true;
    if(!this.validationTable()) {
      return
    }
    await this.cartService.saveOrder()
  }

  validationTable() {
    if ((this.table() <= 0 || this.cart().length <= 0) && this.selected) {
      this.message = this.cart().length === 0 ? "Selecione un menu" : "Seleccione la mesa para poder continuar";
      return false;
    }
    return true;
  }

  handlerAccept() {
    this.router.navigate(['/app/tables'])
  }
}
