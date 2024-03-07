import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { firstValueFrom } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsersService {
  
  private httpClient = inject(HttpClient);
  private baseUrl: string;
  user: any;

  constructor() {
    this.baseUrl = 'http://localhost:8000/auth'
  }

  login(formValue: any) {
    return firstValueFrom(
      this.httpClient.post<any>(`${this.baseUrl}`, formValue)
    )
  }

  chargeUser(user: any) {
    this.user = user;
  }
}
