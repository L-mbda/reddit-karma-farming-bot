#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from praw import Reddit
from utils import random_string


class RedditAPI():
  def __init__(self,
              reddit_client_id,
              reddit_client_secret,
              reddit_password,
              reddit_username):

    self.client_id = reddit_client_id
    self.client_secret = reddit_client_secret
    self.password = reddit_password
    self.username = reddit_username
    self.user_agent = random_string(10)
    self.api = Reddit(
        client_id=self.client_id,
        client_secret=self.client_secret,
        password=self.password,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        username=self.username,
    )
