import { Component, Input } from '@angular/core';
import { Menu } from '../../../../shared/models/menu.model';

@Component({
  selector: 'app-menu-selected',
  standalone: true,
  imports: [],
  templateUrl: './menu-selected.component.html'
})
export class MenuSelectedComponent {
  @Input({ required: true }) menu!: Menu;
}
