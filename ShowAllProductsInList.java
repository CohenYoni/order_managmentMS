import java.awt.Font;
import javax.swing.JFrame;
import javax.swing.JLabel;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import javax.swing.JScrollPane;

public class ShowAllProductsInList {
	  public static void main(String[] args) throws JSONException {
		JSONObject outPutJson = new JSONObject(); 
		try {
			if (args.length != 1)
			      throw new Exception("You need to pass one argument");
			outPutJson = new JSONObject("{ \"hadError\": \"false\", \"error\": \"None\"}");
			//String test = "{ 'products' : [{ 'prodID' : 3, 'prodName' : 'table', 'price' : 50}, { 'prodID' : 2, 'prodName' : 'bag', 'price' : 100}, { 'prodID' : 3, 'prodName' : 'bag', 'price' : 100}]}";
			JSONObject json = new JSONObject(args[0]);
			JSONArray jsonArr = json.getJSONArray("products");
			JFrame frame = new JFrame("Products");
			String allProducts = "";
			allProducts+="<html>";
			
			// Insert products into string.
			for (int i = 0; i < jsonArr.length(); i++) {
				JSONObject product = jsonArr.getJSONObject(i);
				allProducts+=("--Product ")+(Integer.toString(i+1))+"--<br/>";
				allProducts+=("product id : ")+product.getInt("prodID")+"<br/>";
				allProducts+=("product name : ")+product.getString("prodName")+"<br/>";
				allProducts+=("price : ")+product.getInt("price")+"<br/><br/>";
				}
			allProducts+="</html>";
			
			JLabel label = new JLabel(allProducts);
			label.setFont(new Font("Ariel", Font.PLAIN, 15));
			
			// Show all products in list.
			frame.getContentPane().add(new JScrollPane(label));
		    frame.setSize(800, 350);
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