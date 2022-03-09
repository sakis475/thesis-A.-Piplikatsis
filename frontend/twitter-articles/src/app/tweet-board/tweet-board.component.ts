import { Component, OnInit } from '@angular/core';
import { Tweet } from '../interfaces';
import { ChangeArticlesService } from '../services/change-articles.service';
import { GetDataService } from '../services/get-data.service';
@Component({
  selector: 'app-tweet-board',
  templateUrl: './tweet-board.component.html',
  styleUrls: ['./tweet-board.component.scss'],
})
export class TweetBoardComponent implements OnInit {
  public tweets: Tweet[] = [];
  public allTweets: Tweet[] = [];
  public hashtagSelected: string = '';
  constructor(
    private getData: GetDataService,
    private changeArticle: ChangeArticlesService
  ) {}

  ngOnInit(): void {
    this.changeArticle.data$.subscribe((data) => {
      this.hashtagSelected = data;
      this.tweets = this.allTweets.filter(
        (element) => element.searchQuery === data
      );
    });

    this.changeArticle.changePageTweets$.subscribe((data) => {
      if (data === '') {
        data = 0;
      }
      this.getData.getTweetsApi(data).subscribe(async (result) => {
        this.allTweets = await result;
      });
    });
  }
}
