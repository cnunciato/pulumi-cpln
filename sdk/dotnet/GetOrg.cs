// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Cpln
{
    public static class GetOrg
    {
        /// <summary>
        /// Output the ID and name of the current [org](https://docs.controlplane.com/reference/org). 
        /// 
        /// ## Outputs
        /// 
        /// The following attributes are exported:
        /// 
        /// - **cpln_id** (String) The ID, in GUID format, of the Org.
        /// - **name** (String) The name of Org.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Cpln = Pulumi.Cpln;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var org = Cpln.GetOrg.Invoke();
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["orgId"] = org.Apply(getOrgResult =&gt; getOrgResult.Id),
        ///         ["orgName"] = org.Apply(getOrgResult =&gt; getOrgResult.Name),
        ///     };
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetOrgResult> InvokeAsync(InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetOrgResult>("cpln:index/getOrg:getOrg", InvokeArgs.Empty, options.WithDefaults());

        /// <summary>
        /// Output the ID and name of the current [org](https://docs.controlplane.com/reference/org). 
        /// 
        /// ## Outputs
        /// 
        /// The following attributes are exported:
        /// 
        /// - **cpln_id** (String) The ID, in GUID format, of the Org.
        /// - **name** (String) The name of Org.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Cpln = Pulumi.Cpln;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var org = Cpln.GetOrg.Invoke();
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["orgId"] = org.Apply(getOrgResult =&gt; getOrgResult.Id),
        ///         ["orgName"] = org.Apply(getOrgResult =&gt; getOrgResult.Name),
        ///     };
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetOrgResult> Invoke(InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetOrgResult>("cpln:index/getOrg:getOrg", InvokeArgs.Empty, options.WithDefaults());
    }


    [OutputType]
    public sealed class GetOrgResult
    {
        public readonly string CplnId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;

        [OutputConstructor]
        private GetOrgResult(
            string cplnId,

            string id,

            string name)
        {
            CplnId = cplnId;
            Id = id;
            Name = name;
        }
    }
}