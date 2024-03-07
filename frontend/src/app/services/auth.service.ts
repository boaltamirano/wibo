import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { firstValueFrom } from 'rxjs';
import { Auth } from '../shared/models/auth.model';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private httpClient = inject(HttpClient);
  private baseUrl: string;

  constructor() {
    this.baseUrl = 'http://localhost:8000/auth'
  }

  login(formValue: any) {
    return firstValueFrom(
      this.httpClient.post<Auth>(`${this.baseUrl}`, formValue)
    )
  }

}
