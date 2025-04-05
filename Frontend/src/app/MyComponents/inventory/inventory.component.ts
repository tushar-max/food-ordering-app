import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { InventoryService } from 'src/app/Services/BookStoreOwner/inventory.service';
import { Menu } from 'src/app/models/Dishes/menu.model';
import { Books } from 'src/app/models/books.model';

@Component({
  selector: 'app-inventory',
  templateUrl: './inventory.component.html',
  styleUrls: ['./inventory.component.css']
})
export class InventoryComponent {
  // it will store inventory
  public inventory: Menu[] = [];
  dishId: number = -1;
  dishIdx: number = 0;
  editModel = {
    "id":0,
    "name":'',
    "price":0,
    "description":''
  }
  // Constructor for importing routes and services.

  constructor(private route: Router, private inventoryService: InventoryService) { }


  // It will execute when this component is initialized

  ngOnInit(): void {
    this.inventoryService.getInventory().subscribe({
      next: (response) => {
        this.inventory = response;
        console.log(this.inventory);
      },
      error: (err) => {
        console.log(err);
      }
    })
  }


  handleViewDishClick(id: number) {
    this.route.navigate(['dish/'+id])
  }

  handleEditDishClick(idx: number) {
    this.dishIdx=idx;
    this.editModel={
      "id":this.inventory[idx].id,
      "name":this.inventory[idx].name,
      "price":this.inventory[idx].price,
      "description":this.inventory[idx].description
    }
  }

  handleDetailedView() {
    this.route.navigate(['/dish/' + this.dishId]);
  }

  // delete the inventory item
  handleDelete(index:number){
    this.inventoryService.deleteDish(this.inventory[index].id).subscribe({
      next: (response) => {
        console.log(response);
        this.ngOnInit();
      },
      error: (err) => {
        console.log(err);
      }
    })
  }
    // isLoggedIn function will return true if user is loggedin otherwise false

  isLoggedIn() {
    return !(localStorage.getItem("isLoggedIn") === null || localStorage.getItem("isLoggedIn") === '0');
  }
      // isAdmin function will return true if storeowner is loggedin otherwise false

  isAdmin() {
    return !(localStorage.getItem("isAdmin") === null || localStorage.getItem("isAdmin") === '0');
  }

  // this will edit dish
  handleEditDish(){

    if(this.editModel.name==="" || this.editModel.description===""){
      alert("Fields should not be empty");
      return;
    }
    else if(this.editModel.price<=0 || this.editModel.price>1000){
      alert("Price should be in the range of 1 to 1000 rupees");
      return;
    }
    console.log(this.editModel);
    this.inventoryService.editDish(this.editModel).subscribe({
      next:(response)=>{
        console.log(response);
        this.route.navigate(['/inventory']);
      },
      error:(err)=>{
        console.log(err);
      }
    })
    this.ngOnInit();
  }
}
