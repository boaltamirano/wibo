import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Product } from '../../../../shared/models/product.model';
import { CommonModule } from '@angular/common';
import { Menu } from '../../../../shared/models/menu.model';

@Component({
  selector: 'app-menu',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './menu.component.html',
  styleUrl: './menu.component.css'
})
export class MenuComponent {
  @Input({ required: true }) menu!: Menu;

  @Output() addToCart = new EventEmitter();

  addToCartHandler() {
    this.addToCart.emit(this.menu) // envio desde la seccion de producto.component a list.component
  }
}
