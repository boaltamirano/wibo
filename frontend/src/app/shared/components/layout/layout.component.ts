import { Component } from '@angular/core';
import { SideBarComponent } from '../side-bar/side-bar.component';
import { HeaderComponent } from '../header/header.component';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { PageSelectedComponent } from '../../../modules/menus/pages/page-selected/page-selected.component';

@Component({
  selector: 'app-layout',
  standalone: true,
  imports: [SideBarComponent, HeaderComponent, RouterOutlet, CommonModule, PageSelectedComponent],
  templateUrl: './layout.component.html'
})
export class LayoutComponent {

}
