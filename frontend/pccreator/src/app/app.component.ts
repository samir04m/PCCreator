import { Component, OnInit } from '@angular/core';
import { TokenStorageService } from './_services/token-storage.service';
import { ApiService } from './services/api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent implements OnInit {
  title = 'pccreator';

  isLoggedIn = false;
  showAdminBoard = false;
  showModeratorBoard = false;
  username: string;

  pcs:any[];
  

  constructor(private api: ApiService, private tokenStorageService: TokenStorageService) {
    this.getPcs();
  }

  ngOnInit() {
    this.isLoggedIn = !!this.tokenStorageService.getToken();

    if (this.isLoggedIn) {
      const username = this.tokenStorageService.getUserId();
      this.username = username;
    }
  }
  
  getPcs = () => {
    this.api.getPcs().subscribe(
      data => {
        this.pcs = data;
      }, error => {
        console.error(error);
      }
    )
  }

  logout() {
    this.tokenStorageService.signOut();
    window.location.reload();
  }

}
