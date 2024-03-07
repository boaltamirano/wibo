import { Component, inject } from '@angular/core';
import { Router, RouterLinkActive, RouterLinkWithHref } from '@angular/router';

@Component({
  selector: 'app-side-bar',
  standalone: true,
  imports: [RouterLinkWithHref, RouterLinkActive],
  templateUrl: './side-bar.component.html',
  styleUrl: './side-bar.component.css'
})
export class SideBarComponent {

  router = inject(Router)

  onClickLogout() {
    localStorage.clear()
    this.router.navigate(['login'])
  }
}
