import { CommonModule } from '@angular/common';
import { Component, inject } from '@angular/core';
import { TableComponent } from '../../components/table/table.component';
import { Router } from '@angular/router';
import { OrdersService } from '../../../../services/orders.service';

@Component({
  selector: 'app-table-page',
  standalone: true,
  imports: [CommonModule, TableComponent],
  templateUrl: './table-page.component.html',
  styleUrl: './table-page.component.css'
})
export class TablePageComponent {

  tablesNumber = Array(6).fill(null);
  private tableService = inject(OrdersService)

  constructor(
    private router: Router
  ) { }

  viewTable(table: number) {
    // this.cartService.addToCart(product)
    this.router.navigate(['/app/menus'])
    this.tableService.updateOrder(table)
    console.log(table)
  }

}
