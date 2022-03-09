import { Component, OnInit } from '@angular/core';
import { GetDataService } from '../services/get-data.service';

@Component({
  selector: 'app-best-results',
  templateUrl: './best-results.component.html',
  styleUrls: ['./best-results.component.scss'],
})
export class BestResultsComponent implements OnInit {
  public highCosResults;
  public repeatedTrendsResults;
  public freshTrendsResults;

  constructor(private getData: GetDataService) {}

  ngOnInit(): void {
    this.getData.getTopSimilTrends().subscribe(async (result) => {
      this.highCosResults = await result;
    });
    this.getData.getRepeatedTrends().subscribe(async (result) => {
      this.repeatedTrendsResults = await result;
    });
    this.getData.getFreshTrends().subscribe(async (result) => {
      this.freshTrendsResults = await result;
    });
  }
}
