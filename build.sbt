
name := "SparkInAction2-Chapter01"

version := "1.0.0"

scalaVersion := "2.13.6"

val sparkVersion = "2.4.4"

resolvers ++= Seq(
  "apache-snapshots" at "https://repository.apache.org/snapshots/"
)

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core_2.13" % "2.13",
  "org.apache.spark" %% "spark-sql" % "2.13"
)

assemblyMergeStrategy in assembly := {
  case PathList("META-INF", xs @ _*) => MergeStrategy.discard
  case x => MergeStrategy.first
}