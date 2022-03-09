import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-counts-db',
  templateUrl: './counts-db.component.html',
  styleUrls: ['./counts-db.component.scss'],
})
export class CountsDBComponent implements OnInit {
  public counts;

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.getCounts();
  }

  getCounts() {
    this.http
      .get('http://' + environment.HOST + ':5000/countstats')
      .subscribe((counts) => {
        this.counts = counts[0];
      });
  }
}
