import javax.swing.JOptionPane;
import org.json.JSONArray;
import org.json.JSONObject;

public class ShowAllProductsInList {
	  public static void main(String[] args) throws Exception {
		//String structureOfJson = { products: [] };
		try {
			if (args.length != 1)
			      throw new Exception("You need to pass one argument");
			
			//String test = "{ 'products' : [{ 'prodID' : 3, 'prodName' : 'table', 'price' : 50}, { 'prodID' : 2, 'prodName' : 'bag', 'price' : 100}]}";
			JSONObject json = new JSONObject(args[0]);
			JSONArray jsonArr = json.getJSONArray("products");
			String stringOfAllProducts = "";
			
			for (int i = 0; i < jsonArr.length(); i++) {
				JSONObject product = jsonArr.getJSONObject(i);
				stringOfAllProducts+=("Product ")+(Integer.toString(i+1))+"\n";
				stringOfAllProducts+=("product id : ")+product.getInt("prodID")+"\n";
				stringOfAllProducts+=("product name : ")+product.getString("prodName")+"\n";
				stringOfAllProducts+=("price : ")+product.getInt("price")+"\n\n";
				}
			// Show all the products in list.
			JOptionPane.showMessageDialog(null, stringOfAllProducts);
		}
		catch(Exception err) {
			System.out.println(err);
		}
		//finally:
		//	System.out.println(structureOfJson);
}
}
