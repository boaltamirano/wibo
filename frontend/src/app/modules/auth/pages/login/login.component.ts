import { Component } from '@angular/core';
import { LoginFormComponent } from '../../components/login-form/login-form.component';
import { BackgroundComponent } from '../../components/background/background.component';
import { HeaderComponent } from '../../components/header/header.component';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [LoginFormComponent, BackgroundComponent, HeaderComponent],
  templateUrl: './login.component.html'
})
export class LoginComponent {

}
