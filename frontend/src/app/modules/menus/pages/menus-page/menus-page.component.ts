import { Component, inject, signal } from '@angular/core';
import { CartService } from '../../../../services/cart.service';
import { CommonModule } from '@angular/common';
import { MenuComponent } from '../../components/menu/menu.component';
import { MenusService } from '../../../../services/menus.service';
import { Menu } from '../../../../shared/models/menu.model';

@Component({
  selector: 'app-menus-page',
  standalone: true,
  imports: [CommonModule, MenuComponent],
  templateUrl: './menus-page.component.html'
})
export class MenusPageComponent {
  private cartService = inject(CartService);

  menus = signal<Menu[]>([]);
  private menuService = inject(MenusService)

  ngOnInit() {
    this.menuService.getMenus()
    .subscribe({
      next: (menus) => {
        this.menus.set(menus?.body);
      },
      error: () => {

      }
    })
  }

  addToCart(menu: Menu) {
    this.cartService.addToCart(menu)
  }
}
