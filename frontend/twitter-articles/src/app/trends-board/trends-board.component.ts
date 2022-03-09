import { HttpClient } from '@angular/common/http';
import { ThisReceiver } from '@angular/compiler';
import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { NumberValueAccessor } from '@angular/forms';
import { ArticlesBoardComponent } from '../articles-board/articles-board.component';
import { Trend, Article } from '../interfaces';
import { ChangeArticlesService } from '../services/change-articles.service';
import { GetDataService } from '../services/get-data.service';

@Component({
  selector: 'app-trends-board',
  templateUrl: './trends-board.component.html',
  styleUrls: ['./trends-board.component.scss'],
})
export class TrendsBoardComponent implements OnInit {
  public trends: Trend[] = [];
  public articles: Article[] = [];
  public resultsDate: Date = new Date();

  public dateNumButton: number = 0;
  constructor(
    private changeArticle: ChangeArticlesService,
    private getData: GetDataService,
    private http: HttpClient
  ) {}

  ngOnInit(): void {
    this.getData
      .getTrendsApi(this.changeArticle.currentTimestamp)
      .subscribe(async (result) => {
        this.trends = await this.findUniqueTrends(result);
        this.resultsDate = this.trends[0].bestResultsDate;

        this.changeArticle.changePageArticle$.next(result);
        this.changeArticle.changePageTweets$.next(result);
      });

    this.changeArticle.changeTimestamp$.subscribe((data) => {
      if (data) {
        this.getData.getTrendsApi(data).subscribe(async (result) => {
          this.trends = await this.findUniqueTrends(result);
          this.resultsDate = this.trends[0].bestResultsDate;

          this.changeArticle.changePageArticle$.next(data);
          this.changeArticle.changePageTweets$.next(data);
        });
      }
    });
  }

  async findUniqueTrends(result: Trend[]) {
    let excludeDuplicates: string[] = [];
    let uniqueTrends: Trend[] = [];

    for (let res of result) {
      if (excludeDuplicates.includes(res.searchQuery)) {
        console.log('found in exc');
        excludeDuplicates.push(res.searchQuery);
      } else {
        uniqueTrends.push(res);
        excludeDuplicates.push(res.searchQuery);
      }
    }
    console.log('uniqueTrends', uniqueTrends);
    return uniqueTrends;
  }

  onClick(searchQuery: string) {
    this.changeArticle.data$.next(searchQuery);
  }
}
