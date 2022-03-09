import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Chart, ChartType } from 'chart.js';
import { environment } from 'src/environments/environment';
import { sourceScore } from '../interfaces';

@Component({
  selector: 'app-stats',
  templateUrl: './stats.component.html',
  styleUrls: ['./stats.component.scss'],
})
export class StatsComponent implements OnInit {
  public counts;

  public barChart;
  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.getSourcesScore();
  }

  getSourcesScore() {
    this.http
      .get('http://' + environment.HOST + ':5000/sourcesscore')
      .subscribe((scores: sourceScore[]) => {
        let scoresSource = [];
        let scoresCosSimil = [];
        let colors = [];
        scores.sort((a, b) => (a.perc > b.perc ? -1 : b.perc > a.perc ? 1 : 0));
        for (let score of scores) {
          scoresSource.push(score.source);
          scoresCosSimil.push(score.perc);
          switch (score.source) {
            case 'protothema.gr':
              colors.push('#f47b23');
              break;
            case 'in.gr':
              colors.push('#0099d8');
              break;
            case 'enikos.gr':
              colors.push('#be1522');
              break;
            case 'kathimerini.gr':
              colors.push('#295264');
              break;
            case 'skai.gr':
              colors.push('#2672fe');
              break;
          }
        }

        var ctx = document.getElementById('pieCount') as HTMLCanvasElement;

        const data = {
          labels: scoresSource,
          datasets: [
            {
              label: 'Βαθμολογία ειδησεογραφικού',
              data: scoresCosSimil,
              backgroundColor: colors,
            },
          ],
        };

        const config = {
          type: 'bar' as ChartType,
          data: data,
          options: {
            scales: {
              y: {
                ticks: {
                  callback: function (value, index, values) {
                    return value + '%';
                  },
                },
              },
            },
          },
        };

        this.barChart = new Chart(ctx, config);
      });
  }
}
