/*
 * Copyright (C) 2014 Katsuya Iida. All rights reserved.
 */

object BenchScala {
  import scala.io._
  import scala.collection.immutable._
  import scala.util.Random
  
  val DATA_SIZE = 5000 * 100
  
  class User(name: String, email: String) {
    var messageList: List[String] = List()
    override def toString = name + " <" + email + ">"
  }
  
  case class TestData(fromId: String, toId: String)
    
  println("Loading: " + DATA_SIZE + " test items")
  
  def indexToId(index: Int) = "id-" + index
  
  val idUserMap: Map[String, User] = {
    val lines = Source.fromFile("userdata.csv").getLines
    val users = for (line <- lines) yield {
      val record = line.split(',')
      new User(record(0), record(2))
    }
    users.toList.zipWithIndex.map(((a: (User, Int)) => {
      val (user, index) = a
      val id = indexToId(index)
      id -> user
    })).toMap
  }
  
  val testDataList: Seq[TestData] = {
    val numUsers = idUserMap.size
    var random = new Random()
    for (i <- 0 until DATA_SIZE) yield {
      val fromId = indexToId(random.nextInt(numUsers))
      val toId = indexToId(random.nextInt(numUsers))
      TestData(fromId, toId)
    }
  }
  
  def test() = {
    for (data <- testDataList) {
      val fromUser = idUserMap(data.fromId)
      val toUser = idUserMap(data.toId)
      val message = fromUser + " to " + toUser
      toUser.messageList = message :: toUser.messageList
    }
  }
  
  def examine() = {
    val numUsers = idUserMap.size
    val random = new Random()
    for (i <- 0 until 3) {
      val id = indexToId(random.nextInt(numUsers))
      val user = idUserMap(id)
      println("To: " + user)
      for (message <- user.messageList) {
        println(message)
      }
    }
  }

  def main(args: Array[String]) {
    System.gc()
    println("start")
    val start = java.lang.System.nanoTime()
    for (i <- 0 until 4) {
      test()
      val end = java.lang.System.nanoTime()
      println("time: " + ((end - start) / 1000000.0))
    }
    // examine()
  }
}
