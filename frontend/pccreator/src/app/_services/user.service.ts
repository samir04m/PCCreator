import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { TokenStorageService } from './token-storage.service';

const API_URL = 'http://localhost:8000/api';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient, private tokenStorage: TokenStorageService) { }

  getUserData(): Observable<any>  {
    let username:string = this.tokenStorage.getUserId();
    return this.http.get(`${API_URL}/user/data/${username}/`, { responseType: 'text' });
  }
  
}