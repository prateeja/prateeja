# Example

## Repositories


1 ![system-design-primer](https://github.com/prateeja/system-design-primer) [2]

Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.
<hr />

2 ![spring-boot](https://github.com/prateeja/spring-boot) [1]

All working examples using spring boot in this repo including actuator, jpa, batch, web, security etc.
<hr />

3 ![awesome-dropwizard](https://github.com/prateeja/awesome-dropwizard) [1]


<hr />

4 ![awesome-devops](https://github.com/prateeja/awesome-devops) [1]

This is my awesome list with all open source and free applications that you can use in your management
<hr />

5 ![awesome-kafka](https://github.com/prateeja/awesome-kafka) [1]

A list about Apache Kafka
<hr />

6 ![awesome-websockets](https://github.com/prateeja/awesome-websockets) [1]

A curated list of Websocket libraries and resources.
<hr />

7 ![awesome-http-benchmark](https://github.com/prateeja/awesome-http-benchmark) [1]

HTTP(S) benchmark tools, testing/debugging, & restAPI (RESTful)
<hr />

8 ![awesome-database-learning](https://github.com/prateeja/awesome-database-learning) [1]

A list of learning materials to understand databases internals
<hr />

9 ![awesome-spark](https://github.com/prateeja/awesome-spark) [1]

A curated list of awesome Apache Spark packages and resources.
<hr />

10 ![awesome-command-line-apps](https://github.com/prateeja/awesome-command-line-apps) [1]

:shell: Use your terminal shell to do awesome things.
<hr />



## Contributed Repositories

Index: 1

Name: first-contributions

URL: https://github.com/firstcontributions/first-contributions

Star: 29771

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
              repositories(first: 500, orderBy: {field:STARGAZERS, direction: DESC}) {
                nodes {
                  name
                  url
                  stargazerCount
                }
              }
              contributionsCollection {
                pullRequestContributionsByRepository(maxRepositories: 500, excludeFirst:true) {
                  repository {
                    name
                    url
                    stargazerCount
                    isPrivate
                  }
                  contributions(first: 500) {
                    nodes {
                      occurredAt
                      pullRequest {
                        title
                        url
                      }
                    }
                  }
                }
                pullRequestContributions(first: 500){
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
