import java.awt.Font;
import javax.swing.JFrame;
import javax.swing.JLabel;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import javax.swing.JScrollPane;

public class ShowAllOrdersInList {
	  public static void main(String[] args) throws JSONException {
		JSONObject outPutJson = new JSONObject(); 
		try {
			if (args.length != 1)
			      throw new Exception("You need to pass one argument");
			outPutJson = new JSONObject("{ \"hadError\": \"true or false\", \"error\": \"some details of the error\"}");
			//String test = "{ 'orders' : [{ 'ordID' : 1234, 'custName' : 'May', 'custPhone' : '050…', 'ordDate' :'24/8/2018','productsIDs': [1, 2, 3]}]}";
			JSONObject json = new JSONObject(args[0]);
			JSONArray jsonArr = json.getJSONArray("orders");
			JFrame frame = new JFrame("orders");
			String allorders = "";
			allorders+="<html>";
			
			// Insert orders into string.
			for (int i = 0; i < jsonArr.length(); i++) {
				JSONObject order = jsonArr.getJSONObject(i);
				allorders+=("--order")+(Integer.toString(i+1))+"--<br/>";
				allorders+=("order id : ")+order.getInt("ordID")+"<br/>";
				allorders+=("customer name : ")+order.getString("custName")+"<br/>";
				allorders+=("customer phone : ")+order.getString("custPhone")+"<br/>";	
				allorders+=("date : ")+order.getInt("ordDate")+"<br/><br/>";
				allorders+=("products IDs : ")+order.get("productsIDs")+"<br/><br/>";
				//for (int i = 0; i < prodIDs.length(); i++) {
					//allorders+=("--product")+(Integer.toString(j+1))+"--<br/>";
					//allorders+=("id : ")+Integer.toString(prodIDs[j])+"<br/>";

				//}
				}
			allorders+="</html>";
			
			JLabel label = new JLabel(allorders);
			label.setFont(new Font("Ariel", Font.PLAIN, 15));
			
			// Show all orders in list.
			frame.getContentPane().add(new JScrollPane(label));
		    frame.setSize(50, 350);
		    frame.setVisible(true);
		    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);	    
		}
		catch(Throwable err) {
			outPutJson = new JSONObject();
			outPutJson.put("hadError", true);
			outPutJson.put("error", err);
		}
		finally
		{
			System.out.println(outPutJson.toString());
		}
}
}