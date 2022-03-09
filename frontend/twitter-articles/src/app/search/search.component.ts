import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Component, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss'],
})
export class SearchComponent implements OnInit {
  @Input() searchKeywords;
  field = {
    choices: ['αρθρο', 'ταση'],
    selected: 'αρθρο',
  };
  searchResults;
  public searchType = 'articleTitle';

  public sortActive = 'articleTitle';

  public sortObject: any = { articleTitle: 1 };

  public filterQuery;

  constructor(private http: HttpClient) {}

  onItemChange(selected) {
    if (selected === 'αρθρο') {
      this.searchType = 'articleTitle';
    } else if (selected === 'ταση') {
      this.searchType = 'searchQuery';
    }

    this.search();
  }
  ngOnInit(): void {
    this.searchKeywords = 'αθηνα';
    this.search();
  }

  async inputSearchCheck(keyword): Promise<boolean> {
    if (/^.*?(?=[\^#%&$\*:<>\?/\{\|\}]).*$/.test(keyword)) {
      return false;
    } else if (/[^\S\r\n]{2,}/.test(keyword)) {
      return false;
    } else {
      return true;
    }
  }

  async search() {
    console.log(this.searchKeywords);

    if (
      this.searchKeywords.trim().length > 2 &&
      (await this.inputSearchCheck(this.searchKeywords))
    ) {
      const config = {
        headers: new HttpHeaders().set('Content-Type', 'application/json'),
      };
      this.http
        .post(
          'http://' + environment.HOST + ':5000/searcharticlesbykeywords',
          {
            searchKeywords: this.searchKeywords.trim(),
            searchType: this.searchType,
            sortObject: JSON.stringify(this.sortObject),
          },
          config
        )
        .subscribe((data) => {
          console.log('postRequest', data);
          this.searchResults = data;
        });
    }
  }

  clickSort(sortBy) {
    if (sortBy === this.sortActive) {
      this.sortActive = '';
      this.sortObject = { [sortBy]: -1 };
      this.search();
    } else {
      this.sortActive = sortBy;
      this.sortObject = { [sortBy]: 1 };

      this.search();
    }
  }
}
