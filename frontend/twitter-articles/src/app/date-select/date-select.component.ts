import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import * as dayjs from 'dayjs';
import { environment } from 'src/environments/environment';
import { ChangeArticlesService } from '../services/change-articles.service';

@Component({
  selector: 'app-date-select',
  templateUrl: './date-select.component.html',
  styleUrls: ['./date-select.component.scss'],
})
export class DateSelectComponent implements OnInit {
  private dateNow: any;

  public currentDate_forInput: string;

  public dt: string;

  public minMaxDates;

  public hoursToPick;

  public enabledHour: boolean;

  constructor(
    private http: HttpClient,
    private changeArticle: ChangeArticlesService
  ) {}

  ngOnInit(): void {
    this.dateNow = dayjs();
    this.currentDate_forInput = this.dateNow.format('YYYY-MM-DD');
    this.dt = this.currentDate_forInput;
    this.getMinMaxDates();

    this.postDateSelected(this.currentDate_forInput);
  }

  modelChanged(date) {
    console.log(date);
    this.postDateSelected(date);
  }

  getMinMaxDates() {
    this.http
      .get('http://' + environment.HOST + ':5000/daterangeresults')
      .subscribe((dates) => {
        this.minMaxDates = dates[0];

        this.enabledHour = this.minMaxDates.max_date;
        console.log('max_date', this.changeArticle.currentTimestamp);
      });
  }

  postDateSelected(date) {
    this.http
      .post('http://' + environment.HOST + ':5000/resultdates?data=' + date, {})
      .subscribe((timestamps) => {
        console.log('postRequest', timestamps);

        this.hoursToPick = (timestamps as string[]).sort(function (a, b) {
          // Turn your strings into dates, and then subtract them
          // to get a value that is either negative, positive, or zero.
          return new Date(a).valueOf() - new Date(b).valueOf();
        });
      });
  }

  getHourBtnClicked(date) {
    this.changeArticle.changeTimestamp$.next(date);
    this.enabledHour = date;
  }
}
