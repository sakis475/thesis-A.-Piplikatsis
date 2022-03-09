export interface Article {
  articleCategory: string;
  articleDate: string;
  articleLink: string;
  articleTitle: string;
  articleSource: string;

  searchQuery: string;
  cosSimil: number;
  resultCompletedDate: Date;
  diffDate: string;

  bestResultsDate: Date;
}

export interface Trend {
  rank: number;
  searchQuery: string;
  volume: number;
  freshness_trend: string;
  dateDiscovered_trend: Date;
  resultCompletedDate: Date;

  bestResultsDate: Date;
}

export interface Tweet {
  RTCount: string;
  date: Date;
  dateSearched: Date;
  fullText: string;
  hashtags: string[];
  searchQuery: string;
  tweetID: string;
  userID: string;
  userScreenName: string;
}

export interface SearchQuery {
  dateDownloaded: Date;
  rank: number;
  hashtag: string;
}

export interface sourceScore {
  source: string;
  cosBigger35: number;
  countArticlesSource: number;
  perc: number;
}
