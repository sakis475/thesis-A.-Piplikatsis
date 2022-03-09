import { HttpClient } from '@angular/common/http';
import {
  Component,
  OnInit,
  Inject,
  Input,
  OnChanges,
  SimpleChanges,
} from '@angular/core';
import { Chart, registerables, ChartType } from 'chart.js';
import { Observable } from 'rxjs';
import { SearchQuery } from '../interfaces';
import { GetDataService } from '../services/get-data.service';
Chart.register(...registerables);
import * as dayjs from 'dayjs';
import { ChangeArticlesService } from '../services/change-articles.service';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-date-chart',
  templateUrl: './date-chart.component.html',
  styleUrls: ['./date-chart.component.scss'],
})
export class DateChartComponent implements OnInit {
  constructor(
    private http: HttpClient,
    private changeArticle: ChangeArticlesService
  ) {}

  public queryData;

  public searchQuery: string;

  public myChart: any;

  public availableHashtags: string[];

  public hashtagSelected;

  public singleBestResult;

  onClick(searchQuery) {
    this.searchQuery = searchQuery;
    //edw na stelnete kai search query gia tash na emfanizontai kai ekei ta apotelesmata.
    this.makeChart();

    this.getTrendsCorrespondingArticle(searchQuery);
  }

  ngOnInit(): void {
    this.changeArticle.data$.subscribe((data) => {
      this.hashtagSelected = data;
      this.onClick(this.hashtagSelected);
    });

    this.searchQuery = 'Επιλέξτε κάποιο hashtag';
    this.makeChart();

    //pare ola ta diathesima hashtags
    this.getAvailableSearchQuerys();
  }

  async makeData() {
    let dates = [];
    let ranks = [];

    //apo to megalitero sto mikrotero
    let dateRange = this.giveDateRange();
    let rankInRange = [];

    await this.getSearchQuery(this.searchQuery);

    for (let trend of this.queryData) {
      let date = dayjs(trend.dateDownloaded).subtract(2, 'hour');

      dates.push(date);

      //mesa se mia bdomada tha prepei na yparxoun ranks (1,2,3,4,5) kai 0 pou na dilwnei thn eksafanish tou apo ta trends
      ranks.push(trend.rank);
    }

    for (
      let dateRanIndex = 0;
      dateRanIndex < dateRange.length;
      dateRanIndex += 1
    ) {
      for (let dateIndex in dates) {
        if (
          dates[dateIndex].isBefore(dateRange[dateRanIndex]) &&
          dates[dateIndex].isAfter(dateRange[dateRanIndex + 1])
        ) {
          rankInRange.push(ranks[dateIndex]);
          break;
        }
      }
      if (dateRanIndex == rankInRange.length) {
        rankInRange.push('notFound');
      }
    }

    return [dateRange, rankInRange];
  }

  async makeChart() {
    let makeData = await this.makeData();
    let dateRange = makeData[0];
    let rankInRange = makeData[1];

    var ctx = document.getElementById('myChart') as HTMLCanvasElement;

    const labels = dateRange
      .map((x) => {
        if (x.day() === 0) {
          return x.format('DD-MM') + ' Κυριακή ' + x.format('HH:mm');
        } else if (x.day() === 1) {
          return x.format('DD-MM') + ' Δευτέρα ' + x.format('HH:mm');
        } else if (x.day() === 2) {
          return x.format('DD-MM') + ' Τρίτη ' + x.format('HH:mm');
        } else if (x.day() === 3) {
          return x.format('DD-MM') + ' Τετάρτη ' + x.format('HH:mm');
        } else if (x.day() === 4) {
          return x.format('DD-MM') + ' Πέμπτη ' + x.format('HH:mm');
        } else if (x.day() === 5) {
          return x.format('DD-MM') + ' Παρασκευή ' + x.format('HH:mm');
        } else {
          return x.format('DD-MM') + ' Σαββάτο ' + x.format('HH:mm');
        }
      })
      .reverse();
    const data = {
      labels: labels,
      datasets: [
        {
          label: this.searchQuery,
          backgroundColor: 'rgb(255, 99, 132)',
          borderColor: 'rgb(255, 99, 132)',
          //data= request.get(rank)
          data: rankInRange.reverse(),
          pointRadius: 4,
          pointHoverRadius: 8,
        },
      ],
    };
    const config = {
      responsive: true,
      maintainAspectRatio: false,
      type: 'line' as ChartType,
      data: data,
      options: {
        plugins: {
          title: {
            display: true,
            text: 'Εμφάνιση της τάσης την τελευταία βδομάδα',
          },
          subtitle: {
            display: true,
            text: 'Κάθε κουκίδα αντιπροσωπεύει την κατάταξη του trend, την στιγμή που βρέθηκε',
          },
        },
        pointStyle: 'circle',
        //pointBackgroundColor: 'white',
        scales: {
          x: {
            display: true,
            title: {
              display: true,
              text: 'Άξονας Χ: Ημερομηνία από τώρα (τελευταία δεξιά) μέχρι πίσω μια βδομάδα (προς τα αριστερά)',
            },
          },
          y: {
            display: true,
            title: {
              display: true,
              text: 'Άξονας Υ: Κατάταξη',
            },
            ticks: {
              maxTicksLimit: 5,
              stepSize: 1,
            },
            afterDataLimits: (scale) => {
              scale.max = 5;
              scale.min = 1;
            },
            reverse: true,
          },
        },
      },
    };
    if (this.myChart) {
      this.myChart.data.datasets = data.datasets;
      this.myChart.update();
    } else {
      this.myChart = new Chart(ctx, config);
    }
  }

  giveDateRange() {
    let datenow: any = dayjs();
    datenow = datenow
      .subtract(datenow.minute(), 'minute')
      .subtract(datenow.millisecond(), 'millisecond')
      .subtract(datenow.second(), 'second')
      .add(3, 'hour');
    let createDateRange = [];
    //ana 3 wres dimiourgei date
    for (let i = 0; i < 7 * 24; i += 3) {
      createDateRange.push(datenow.subtract(i, 'hours'));
    }
    return createDateRange;
  }

  async getSearchQuery(searchQuery: string) {
    const pathSearchQuery = 'http://' + environment.HOST + ':5000/searchquery';
    this.queryData = await this.http
      .get(pathSearchQuery + '?data=' + encodeURIComponent(searchQuery))
      .toPromise();
  }

  async getAvailableSearchQuerys() {
    const pathSearchQuery = 'http://' + environment.HOST + ':5000/searchquery';
    let results: string[] = await this.http
      .get<string[]>(pathSearchQuery)
      .toPromise();
    this.availableHashtags = results;
  }

  async getTrendsCorrespondingArticle(trend) {
    const pathSearchQuery =
      'http://' + environment.HOST + ':5000/gettrendscorrespondingarticle';
    this.singleBestResult = await this.http
      .get(pathSearchQuery + '?data=' + encodeURIComponent(trend))
      .toPromise();
  }
}
