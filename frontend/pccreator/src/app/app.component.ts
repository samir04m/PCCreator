import { Component } from '@angular/core';
import { ApiService } from './services/api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {
  title = 'pccreator';
  
  pcs = [{
    name : 'prueba'
  }];

  constructor(private api:ApiService) {
    this.getPcs();
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

}
