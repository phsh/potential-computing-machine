import com.couchbase.client.CouchbaseClient;
import java.net.URI;
import java.util.Arrays;
import java.util.List;
 
public class LoadData {
 
  public static void main(String[] args) throws Exception {
 
    // (Subset) of nodes in the cluster to establish a connection
    List<URI> hosts = Arrays.asList(
      new URI("http://127.0.0.1:8091/pools")
    );
 
    // Name of the Bucket to connect to
    String bucket = "jawa-sample";
 
    // Password of the bucket (empty) string if none
    String password = "";
 
    // Connect to the Cluster
    CouchbaseClient client = new CouchbaseClient(hosts, bucket, password);
 
    // Store a Document
    client.set("Per", "{\"firstname\":\"Per\",\"lastname\":\"Andersson\",\"age\":\"23\"}").get();
    client.set("Johan", "{\"firstname\":\"Johan\",\"lastname\":\"Person\",\"age\":\"34\"}").get();
    client.set("Anders", "{\"firstname\":\"Anders\",\"lastname\":\"Johansson\",\"age\":\"45\"}").get();
    client.set("Sigge", "{\"firstname\":\"Sigge\",\"lastname\":\"Hansson\",\"age\":\"56\"}").get();
    client.set("Kent", "{\"firstname\":\"Kent\",\"lastname\":\"Karlsson\",\"age\":\"67\"}").get();
 
    // Retreive the Document and print it
    //System.out.println(client.get("my-first-document"));
 
    // Shutting down properly
    client.shutdown();
  }
}