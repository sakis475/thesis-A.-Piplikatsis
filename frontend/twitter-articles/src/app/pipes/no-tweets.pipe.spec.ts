import { NoTweetsPipe } from './no-tweets.pipe';

describe('NoTweetsPipe', () => {
  it('create an instance', () => {
    const pipe = new NoTweetsPipe();
    expect(pipe).toBeTruthy();
  });
});
