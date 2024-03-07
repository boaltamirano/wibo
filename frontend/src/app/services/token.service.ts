import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { firstValueFrom } from 'rxjs';
import { Auth } from '../shared/models/auth.model';

@Injectable({
  providedIn: 'root'
})
export class TokenService {

  constructor() {

  }

  saveToken(token: string) {
    localStorage.setItem('token', token)
  }

  getToken() {
    const token = localStorage.getItem('token')
    return token;
  }

  removeToken() {
    localStorage.removeItem("token")
  }

}
