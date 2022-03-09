import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ChangeArticlesService {
  public currentHashtag: string = '';
  public currentTimestamp = '';
  public data$: BehaviorSubject<any> = new BehaviorSubject(this.currentHashtag);

  public changePageArticle$: BehaviorSubject<any> = new BehaviorSubject(
    this.currentHashtag
  );

  public changePageTweets$: BehaviorSubject<any> = new BehaviorSubject(
    this.currentHashtag
  );

  public changeTimestamp$: BehaviorSubject<any> = new BehaviorSubject(
    this.currentTimestamp
  );

  constructor(public http: HttpClient) {}
}
