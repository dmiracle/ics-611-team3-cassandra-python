
One of the common uses of distributed databases is in the online advertising world. This is responsible for funding most of what is on the web these days. This app is meant to offer up any surface with a monitor as a place to sell ads. The app flow goes something like this:

App geolocates user
App pulls demographic data 
App auctions off screen by matching demographics with ad demographics
App load ad
App pay user


## Stack
- cassandra
    - datastax
- python

## Process
- Start with 2 census csvs 
- filter and merge into the demographics table
- Send address to app (geolocate)
- Pull demographic info based on census tract
- Auction ad space based on demographics
- Load adertisement
- Pay user

## Datamodel
- tables and image

## Architectural considerations

How do we design for using cassandra vs mysql
- Denormalization
- filter and merge into the table we use in the end
    this is an important step for NoSQL arch bc it means we are preventing us from ahving to do complex qeries and creating a table that reflects what we will want to know
- loaded as a csv into cassandra (datastax)

Each step has a table associated with it -- data is modeled based on the query pattern (to an extreme)
Always searching by primary index

Eveventual consistency is fine, more important to be up because targeted ads are not super critical if they are not consitent all the time.
