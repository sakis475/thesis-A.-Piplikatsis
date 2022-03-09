import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { SearchQuery } from '../interfaces';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root',
})
export class GetDataService {
  pathTrends: string = 'http://' + environment.HOST + ':5000/trends';
  pathArticles: string = 'http://' + environment.HOST + ':5000/articles';
  pathTweets: string = 'http://' + environment.HOST + ':5000/tweets';
  pathTopSimilTrends: string =
    'http://' + environment.HOST + ':5000/topsimiltrends';

  pathFresh_OldTrends: string =
    'http://' + environment.HOST + ':5000/freshnesstrend';

  constructor(private http: HttpClient) {}

  // get data
  getTrendsApi(dateBack: string): Observable<any> {
    console.log('dateBack', dateBack);

    return this.http.get(this.pathTrends + '?data=' + dateBack);
  }

  getArticlesApi(dateBack: string): Observable<any> {
    return this.http.get(this.pathArticles + '?data=' + dateBack);
  }

  getTweetsApi(dateBack: string): Observable<any> {
    return this.http.get(this.pathTweets + '?data=' + dateBack);
  }

  getTopSimilTrends(): Observable<any> {
    return this.http.get(this.pathTopSimilTrends);
  }

  getFreshTrends(): Observable<any> {
    return this.http.get(this.pathFresh_OldTrends + '?data=new');
  }

  getRepeatedTrends(): Observable<any> {
    return this.http.get(this.pathFresh_OldTrends + '?data=old');
  }
}
