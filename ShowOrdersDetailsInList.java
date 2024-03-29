
import java.awt.Font;
import javax.swing.JFrame;
import javax.swing.JLabel;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import javax.swing.JScrollPane;

public class ShowOrdersDetailsInList {
	  public static void main(String[] args) throws JSONException {
		JSONObject outPutJson = new JSONObject(); 
		try {
			if (args.length != 1)
			      throw new Exception("You need to pass one argument");
			outPutJson = new JSONObject("{ \"hadError\": false, \"error\": \"\"}");
			JSONObject json = new JSONObject(args[0]);

			JSONArray jsonArr = json.getJSONArray("orders");
			JFrame frame = new JFrame("orders");
			String allorders = "";
			allorders+="<html>";
			
			// Insert orders into string.
			for (int i = 0; i < jsonArr.length(); i++) {
				JSONObject order = jsonArr.getJSONObject(i);
				allorders+=("--order ")+(Integer.toString(i+1))+"--<br/>";
				allorders+=("order id : ")+order.getInt("ordID")+"<br/>";
				allorders+=("customer name : ")+order.getString("custName")+"<br/>";
				allorders+=("customer phone : ")+order.getString("custPhone")+"<br/>";	
				allorders+=("date : ")+order.getString("ordDate")+"<br/>";
				JSONArray JprodNames=order.getJSONArray("productsNames");
				allorders+=("products : ");
				
				for (int j = 0; j < JprodNames.length(); j++) {
					allorders+=JprodNames.getString(j);
					if(j+1<JprodNames.length())
						allorders+=", ";
				}
				allorders+="<br/><br/>";
			}
			
			allorders+="</html>";
			
			JLabel label = new JLabel(allorders);
			label.setFont(new Font("Ariel", Font.PLAIN, 15));
			
			// Show all orders in list.
			frame.getContentPane().add(new JScrollPane(label));
		    frame.setSize(700, 350);
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