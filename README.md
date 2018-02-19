# Twitter Flask App

## Flask App to get twitter records

a flask application to get a query from user and find the number of tweets per second, using the new 1.1 twitter API

## Usage:

 Just add `/query/?q=Hasura` (for example we are taking the query to be `Hasura`) to the URL: [https://app.ambitious98.hasura-app.io/](https://app.ambitious98.hasura-app.io/) that will fetch you **recent** *100* results from the twitter and display how many `Hasura` quoted tweets were published in one second.

Example: 
```
Query: Hasura
Tweets per second: 0.0002730166703978945
Oldest Tweet at: Thu Feb 15 04:50:15 +0000 2018
Number of Results: 100

* guide to writing dockerfiles for go webapps: https://t.co/qJl0pmOe4v https://t.co/M8kEVl5RAe
* "Git push" and deploy a rust-rocket app to an HTTPS domain with no setup or configuration! Get started with this bo… https://t.co/0y48KFGX2c
* RT @hintIIITA: We're proud to present @HasuraHQ as our patron! With Hasura, you can build and host powerful applications in minutes. It is…
```
Live demo at: [https://app.ambitious98.hasura-app.io/ ](https://app.ambitious98.hasura-app.io/ )




