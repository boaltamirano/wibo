import { CommonModule } from '@angular/common';
import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { faEye, faEyeSlash, faSignIn } from '@fortawesome/free-solid-svg-icons';
import { UsersService } from '../../../../services/users.service';

@Component({
  selector: 'app-login-form',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, FontAwesomeModule],
  templateUrl: './login-form.component.html'
})
export class LoginFormComponent {

  usersService = inject(UsersService);

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
      const { email, password } = this.form.getRawValue();
      console.log("email: ", this.form.getRawValue())
      const response = await this.usersService.login(this.form.getRawValue())
      console.log(response)
      // TODO
    } else {
      this.form.markAllAsTouched();
    }
  }
}
