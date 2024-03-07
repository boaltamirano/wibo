import { CommonModule } from '@angular/common';
import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { faEye, faEyeSlash, faSignIn } from '@fortawesome/free-solid-svg-icons';
import { UsersService } from '../../../../services/users.service';
import { TokenService } from '../../../../services/token.service';

@Component({
  selector: 'app-login-form',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, FontAwesomeModule],
  templateUrl: './login-form.component.html'
})
export class LoginFormComponent {

  usersService = inject(UsersService);
  tokenService = inject(TokenService);

  form = this.formBuilder.nonNullable.group({
    email: ['', [Validators.email, Validators.required]],
    password: ['', [Validators.required, Validators.minLength(6)]],
  });
  faEye = faEye;
  faEyeSlash = faEyeSlash;
  showPassword = false;
  status: string = 'init';
  faSignIn = faSignIn;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router
  ) { }

  async doLogin() {
    if (this.form.valid) {
      this.status = 'loading';
      const response = await this.usersService.login(this.form.getRawValue())
      if (response?.body[0]?.token) {
        console.log(response?.body[0]?.token)
        this.tokenService.saveToken(response?.body[0]?.token)
        this.router.navigate(['/home'])
      }
      console.log(response)
    } else {
      this.form.markAllAsTouched();
    }
  }
}
