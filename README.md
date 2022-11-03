# Example

## Repositories


Index: 1

Name: system-design-primer

URL: https://github.com/prateeja/system-design-primer

Star: 2

Description: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

<hr />

Index: 2

Name: spring-boot

URL: https://github.com/prateeja/spring-boot

Star: 1

Description: All working examples using spring boot in this repo including actuator, jpa, batch, web, security etc.

<hr />

Index: 3

Name: awesome-dropwizard

URL: https://github.com/prateeja/awesome-dropwizard

Star: 1

Description: 

<hr />

Index: 4

Name: awesome-devops

URL: https://github.com/prateeja/awesome-devops

Star: 1

Description: This is my awesome list with all open source and free applications that you can use in your management

<hr />

Index: 5

Name: awesome-kafka

URL: https://github.com/prateeja/awesome-kafka

Star: 1

Description: A list about Apache Kafka

<hr />

Index: 6

Name: awesome-websockets

URL: https://github.com/prateeja/awesome-websockets

Star: 1

Description: A curated list of Websocket libraries and resources.

<hr />

Index: 7

Name: awesome-http-benchmark

URL: https://github.com/prateeja/awesome-http-benchmark

Star: 1

Description: HTTP(S) benchmark tools, testing/debugging, & restAPI (RESTful)

<hr />

Index: 8

Name: awesome-database-learning

URL: https://github.com/prateeja/awesome-database-learning

Star: 1

Description: A list of learning materials to understand databases internals

<hr />

Index: 9

Name: awesome-spark

URL: https://github.com/prateeja/awesome-spark

Star: 1

Description: A curated list of awesome Apache Spark packages and resources.

<hr />

Index: 10

Name: awesome-command-line-apps

URL: https://github.com/prateeja/awesome-command-line-apps

Star: 1

Description: :shell: Use your terminal shell to do awesome things.

<hr />


## Contributed Repositories

Index: 1

Name: first-contributions

URL: https://github.com/firstcontributions/first-contributions

Star: 29720

Description: 🚀✨ Help beginners to contribute to open source projects

Contributions:

 - Add Prateek Jain to Contributors list


<hr />
Index: 2

Name: system-design-primer

URL: https://github.com/prateeja/system-design-primer

Star: 2

Description: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

Contributions:

 - Merging from source repo
 - Merging from source
 - Fetching updates


<hr />
Index: 3

Name: java-design-patterns

URL: https://github.com/prateeja/java-design-patterns

Star: 1

Description: Design patterns implemented in Java

Contributions:

 - Merging from source repo
 - Pulling from Source
 - Merging from HEAD
 - Fetching updates


<hr />
Index: 4

Name: coding-interview-university

URL: https://github.com/prateeja/coding-interview-university

Star: 1

Description: A complete computer science study plan to become a software engineer.

Contributions:

 - Merging from source repo
 - Merging from source
 - Merging from HEAD
 - Fetching updates


<hr />
Index: 5

Name: awesome-python

URL: https://github.com/prateeja/awesome-python

Star: 1

Description: A curated list of awesome Python frameworks, libraries, software and resources

Contributions:

 - Merging from source repo
 - Fetching updates


<hr />
Index: 6

Name: awesome-scalability

URL: https://github.com/prateeja/awesome-scalability

Star: 1

Description: The Patterns of Scalable, Reliable, and Performant Large-Scale Systems

Contributions:

 - Merging from source repo
 - Fetching updates


<hr />
Index: 7

Name: build-your-own-x

URL: https://github.com/prateeja/build-your-own-x

Star: 1

Description: 🤓 Build your own (insert technology here)

Contributions:

 - Merging from source repo
 - Fetching updates


<hr />
Index: 8

Name: awesome-data-engineering

URL: https://github.com/prateeja/awesome-data-engineering

Star: 1

Description: A curated list of data engineering tools for software developers

Contributions:

 - Merging from source repo
 - Fetching updates


<hr />
Index: 9

Name: public-apis

URL: https://github.com/prateeja/public-apis

Star: 1

Description: A collective list of free APIs for use in software and web development.

Contributions:

 - Merging from source repo
 - Fetching updates


<hr />
Index: 10

Name: free-programming-books

URL: https://github.com/prateeja/free-programming-books

Star: 1

Description: :books: Freely available programming books

Contributions:

 - Merging from source repo
 - Merging from HEAD


<hr />


```graphQL
query {
            user(login: "ntsd") {
              name
              repositories(first: 10, orderBy: {field:STARGAZERS, direction: DESC}) {
                nodes {
                  name
                  url
                  stargazerCount
                }
              }
              contributionsCollection {
                pullRequestContributionsByRepository(maxRepositories: 100, excludeFirst:true) {
                  repository {
                    name
                    url
                    stargazerCount
                    isPrivate
                  }
                  contributions(first: 10) {
                    nodes {
                      occurredAt
                      pullRequest {
                        title
                        url
                      }
                    }
                  }
                }
                pullRequestContributions(first: 5){
                  nodes{
                   pullRequest {
                     title
                      repository {
                        name
                        url
                      }
                   }
                  }
                }
                totalRepositoriesWithContributedPullRequests
                totalRepositoriesWithContributedCommits
              }
            }
          }
```
