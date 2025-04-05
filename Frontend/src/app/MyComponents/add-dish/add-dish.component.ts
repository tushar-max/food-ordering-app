import { Component } from '@angular/core';
import { Route, Router } from '@angular/router';
import { InventoryService } from 'src/app/Services/BookStoreOwner/inventory.service';

@Component({
  selector: 'app-add-dish',
  templateUrl: './add-dish.component.html',
  styleUrls: ['./add-dish.component.css']
})
export class AddDishComponent {
  // dish object
  public dish = {
    "name": '',
    "price": 0,
    "description": '',
    "storeid": localStorage.getItem("userEmail")
  }
  // Constructor for importing routes and inventory service.
  constructor(private router: Router, private inventoryService: InventoryService) { }

  // This method is responsible for adding dish to database
  handleAddDish() {
    if (this.dish.name === "" || this.dish.description === "") {
      alert("Fields should not be empty");
      return;
    }
    else if (this.dish.price <= 0 || this.dish.price > 1000) {
      alert("Price should be in the range of 1 to 1000 rupees");
      return;
    }
    // console.log(this.dish);
    // calling service to add dish
    this.inventoryService.addDish(this.dish).subscribe({
      next: (response) => {
        console.log(response);
        this.dish = {
          "name": '',
          "price": 0,
          "description": '',
          "storeid": localStorage.getItem("userEmail")
        }
        this.router.navigate(['/inventory']);
      },
      error: (err) => {
        console.log(err);
      }
    })
  }
  // isAdmin function will return true if storeowner is loggedin otherwise false

  isAdmin() {
    return !(localStorage.getItem("isAdmin") === null || localStorage.getItem("isAdmin") === '0');
  }
}
