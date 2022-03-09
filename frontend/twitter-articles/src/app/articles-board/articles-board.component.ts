import {
  Component,
  EventEmitter,
  OnInit,
  OnChanges,
  Output,
  ChangeDetectorRef,
} from '@angular/core';
import { Article } from '../interfaces';
import { ChangeArticlesService } from '../services/change-articles.service';
import { GetDataService } from '../services/get-data.service';

@Component({
  selector: 'app-articles-board',
  templateUrl: './articles-board.component.html',
  styleUrls: ['./articles-board.component.scss'],
})
export class ArticlesBoardComponent implements OnInit {
  public allArticles: Article[] = [];
  public articles: Article[] = [];
  public hashtagSelected: string = '';

  constructor(
    private changeArticle: ChangeArticlesService,
    private getData: GetDataService
  ) {}

  ngOnInit(): void {
    this.changeArticle.data$.subscribe((data) => {
      this.hashtagSelected = data;
      this.articles = this.allArticles.filter(
        (element) => element.searchQuery === data
      );
    });

    this.changeArticle.changePageArticle$.subscribe((data) => {
      if (data === '') {
        data = 0;
      }
      this.getData.getArticlesApi(data).subscribe(async (result) => {
        this.allArticles = await result;
      });
    });
  }
}
