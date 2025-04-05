import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { OrderService } from 'src/app/Services/Orders/order.service';
import { BookServicesService } from 'src/app/Services/book-services.service';
import { Menu } from 'src/app/models/Dishes/menu.model';
import { Books } from 'src/app/models/books.model';
import { Reviews } from 'src/app/models/reviews.model';

@Component({
  selector: 'app-view-dish',
  templateUrl: './view-dish.component.html',
  styleUrls: ['./view-dish.component.css']
})
export class ViewDishComponent {
  public id: number = -1;
  public dish: Menu | undefined;
  public quantity: number = 1;
  public reviews: Reviews[] = [];

  // Constructor for importing routes and services.

  constructor(private router: Router, private route: ActivatedRoute, private bookService: BookServicesService, private orderService: OrderService) {

  }
  // It will execute when this component is initialized

  ngOnInit(): void {
    this.id = Number(this.route.snapshot.paramMap.get('id'));
    // get selected dish
    this.bookService.getDishById(this.id).subscribe({
      next: (response) => {
        this.dish = response;
        console.log(this.dish);
      },
      error: (err) => {
        console.log(err);
      }
    })
    // get all dish reviews of a dish

    this.bookService.getBookReviews(this.id).subscribe({
      next: (response) => {
        this.reviews = response;
        console.log(this.reviews);
      },
      error: (err) => {
        console.log(err);
      }
    })
  }

  // place an order

  handleBuyNow() {
    if (this.quantity > 10) {
      alert("You can't buy more than 10 books");
      this.quantity = 1;
    }
    else if (this.quantity < 1) {
      alert("Please add atleast 1 dish");
      this.quantity = 1;
    }
    else {
      const now = new Date();
      let order = {
        "customerid": localStorage.getItem("userEmail"),
        "dishid": this.id,
        "resid": this.dish?.resid,
        "dishtitle": this.dish?.name,
        "orderdate": now.toLocaleDateString(),
        "orderstatus": "Order Placed"
      };

      this.bookService.placeOrder(order).subscribe({
        next: (response) => {
          this.reviews = response;
        },
        error: (err) => {
          console.log(err);
        }
      })

    }
  }

  // add to cart

  handleAddToCart() {
    const cartItem = {
      "customerid": localStorage.getItem("userEmail"),
      "dishid": this.dish?.id,
      "dishtitle": this.dish?.name
    }
    // console.log(cartItem);
    this.orderService.addToCart(cartItem).subscribe({
      next: (response) => {
        console.log(response);
        this.router.navigate(['/cart']);
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
  // isLoggedIn function will return true if user is loggedin otherwise false

  isAdmin() {
    return !(localStorage.getItem("isAdmin") === null || localStorage.getItem("isAdmin") === '0');
  }
}
