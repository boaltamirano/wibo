import { Component, inject } from '@angular/core';
import { SideBarComponent } from '../side-bar/side-bar.component';
import { HeaderComponent } from '../header/header.component';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { OrdersService } from '../../../services/orders.service';

@Component({
  selector: 'app-layout',
  standalone: true,
  imports: [SideBarComponent, HeaderComponent, RouterOutlet, CommonModule],
  templateUrl: './layout.component.html'
})
export class LayoutComponent {

  private tableService = inject(OrdersService)

  table = this.tableService.tableSelected;
}
