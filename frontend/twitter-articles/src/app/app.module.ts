import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TrendsBoardComponent } from './trends-board/trends-board.component';
import { NoTweetsPipe } from './pipes/no-tweets.pipe';
import { ArticlesBoardComponent } from './articles-board/articles-board.component';

import { HttpClientModule } from '@angular/common/http';
import { SimilarityPipe } from './pipes/similarity.pipe';
import { TweetBoardComponent } from './tweet-board/tweet-board.component';

import { ScrollingModule } from '@angular/cdk/scrolling';
import { DiffDatePipe } from './pipes/diff-date.pipe';
import { DateChartComponent } from './date-chart/date-chart.component';
import { HomeComponent } from './home/home.component';
import { BestResultsComponent } from './best-results/best-results.component';
import { SearchComponent } from './search/search.component';
import { FormsModule } from '@angular/forms';
import { DateSelectComponent } from './date-select/date-select.component';
import { StatsComponent } from './stats/stats.component';
import { CountsDBComponent } from './counts-db/counts-db.component';
import { FooterComponent } from './footer/footer.component';

@NgModule({
  declarations: [
    AppComponent,
    TrendsBoardComponent,
    NoTweetsPipe,
    ArticlesBoardComponent,
    SimilarityPipe,
    TweetBoardComponent,
    DiffDatePipe,
    DateChartComponent,
    HomeComponent,
    BestResultsComponent,
    SearchComponent,
    DateSelectComponent,
    StatsComponent,
    CountsDBComponent,
    FooterComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    ScrollingModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
