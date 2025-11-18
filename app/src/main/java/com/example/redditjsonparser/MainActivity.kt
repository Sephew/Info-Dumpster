package com.example.redditjsonparser

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.example.redditjsonparser.ui.theme.RedditjsonparserTheme
import android.widget.ArrayAdapter
import android.widget.ListView
import androidx.appcompat.app.AppCompatActivity
import org.json.JSONObject
import java.io.BufferedReader
import java.io.InputStreamReader
import java.net.HttpURLConnection
import java.net.URL
import kotlin.concurrent.thread
class MainActivity : AppCompatActivity() {

    private lateinit var listView: ListView
    private val postList = ArrayList<String>()

    private val redditUrl = "https://www.reddit.com/r/androiddev/top.json?limit=15"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        listView = findViewById(R.id.listView)

        // Trigger the network request
        fetchRedditData()
    }

    private fun fetchRedditData() {
        thread {
            try {
                val url = URL(redditUrl)
                val conn = url.openConnection() as HttpURLConnection
                conn.requestMethod = "GET"

                //Request a real agent or else we get blocked
                conn.setRequestProperty("User-Agent", "MySchoolProjectApp/1.0")

                // Read the data
                val reader = BufferedReader(InputStreamReader(conn.inputStream))
                val response = StringBuilder()
                var line: String?
                while (reader.readLine().also { line = it } != null) {
                    response.append(line)
                }
                reader.close()

                // Parse the data
                parseRedditJson(response.toString())

            } catch (e: Exception) {
                e.printStackTrace()
                // on failure
                runOnUiThread {
                    postList.add("Error fetching data: ${e.message}")
                    updateList()
                }
            }
        }
    }

    // parse into JSON data
    private fun parseRedditJson(jsonString: String) {
        try {
            // 1. The Root Object
            val root = JSONObject(jsonString)

            // 2. Reddit puts everything inside a "data" object
            val dataObject = root.getJSONObject("data")

            // 3. The actual posts are in a "children" array
            val childrenArray = dataObject.getJSONArray("children")

            // 4. Loop through the posts
            for (i in 0 until childrenArray.length()) {

                // 5. Get the specific post object (it's wrapped in 'data' again)
                val child = childrenArray.getJSONObject(i)
                val postData = child.getJSONObject("data")

                // 6. Retrieve the fields we want
                val title = postData.getString("title")
                val author = postData.getString("author")
                val score = postData.getInt("score")

                // Format for our list
                val displayString = "r/androiddev\nUser: u/$author\nUpvotes: $score\n$title"
                postList.add(displayString)
            }

            // Update the UI list
            runOnUiThread { updateList() }

        } catch (e: Exception) {
            e.printStackTrace()
        }
    }

    private fun updateList() {
        val adapter = ArrayAdapter(
            this,
            android.R.layout.simple_list_item_1,
            postList
        )
        listView.adapter = adapter
    }
}